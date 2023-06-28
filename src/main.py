import argparse

from docx import Document

from src.docx_utils import process_docx_file


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", default="data/input_files/in.docx", help="Input file name")
    parser.add_argument("--output_file", default="data/output_files/out.docx", help="Output file name")
    args, unknown_args = parser.parse_known_args()

    parameters = {}
    for arg in unknown_args:
        if "=" in arg:
            param, value = arg.split("=")
            parameters[param] = value

    process_docx_file(args.input_file, args.output_file, **parameters)
