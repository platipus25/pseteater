import pymupdf
from pymupdf import Rect
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
    prog="pseteater",
    description="Take a pdf of a pset and output svgs for each problem",
)
parser.add_argument("filename", type=argparse.FileType("rb"))
parser.add_argument("-o", "--output", type=Path, default=Path("./"))


def main():
    args = parser.parse_args()

    print("Hello from pseteater!")

    doc = pymupdf.open(args.filename)  # open the document

    for page in doc:  # .pages(1, 2):
        print(f"Processing page {page.number}")

        bb = Rect()

        def add(ourbb):
            include = True
            if not page.mediabox.contains(ourbb):
                # print(ourbb)
                include = False

            increase = (
                Rect(bb).include_rect(ourbb).get_area("in")
                - bb.get_area("in")
                - ourbb.get_area("in")
            )
            # print(increase)
            if increase > 20:
                include = False

            if include:
                bb.include_rect(ourbb)

        for block in page.get_text("blocks", sort=True):
            ourbb = Rect(block[:4])
            # print(block)
            add(ourbb)

        for drawing in page.get_cdrawings():
            ourbb = Rect(drawing["rect"])
            add(ourbb)

        # print(page.mediabox, bb)
        if not page.mediabox.contains(bb):
            print("Bad things!")
            print(page.mediabox, bb)
            # bb = page.mediabox

        page.set_cropbox(bb)

        args.output.mkdir(parents=True, exist_ok=True)
        filename = args.output / f"page{page.number}.svg"
        with open(filename, "+w") as f:
            f.write(page.get_svg_image())

        # print(drawing_list)


if __name__ == "__main__":
    main()
