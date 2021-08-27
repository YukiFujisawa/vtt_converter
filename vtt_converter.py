import glob
import csv
import os

def replace_contents(contents: list) -> str:
    del contents[3:]
    return ''.join(contents)

def replace_with_vtt_file_name(file_name: str) -> str:
    names = file_name.split('_')
    return names[0].replace('inputs', 'outputs') + '_' + names[1] + '_' + names[2] + '_' + names[3][0] + '_ja.vtt'

def main() -> None:
    tsv_file_names = glob.glob("./inputs/*.tsv")
    for tsv_file_name in tsv_file_names:
        with open(tsv_file_name, 'r',encoding='utf-8_sig') as tsv_file:
            vtt_file_name = replace_with_vtt_file_name(tsv_file_name)
            try:
                os.remove(vtt_file_name)
            except OSError as err:
                pass
            for contents in csv.reader(tsv_file, delimiter='\t'):
                content = replace_contents(contents)
                with open(vtt_file_name, 'a') as vtt_file:
                    print(content, file=vtt_file)

if __name__ == "__main__":
    main()


