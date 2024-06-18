import csv
import os

def text_file_to_csv(input_text_file, output_csv_file):    
    with open(input_text_file, 'r') as file:
        lines = file.read().strip().split('\n')

    with open(output_csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(["codigo", "municipio"])
        
        for i in range(1, len(lines) - 1, 2):
            print(i)
            municipio = lines[i]
            codigo = lines[i + 1]
            writer.writerow([codigo, municipio])
    
    print(f"Finalizou transcrição em CSV")

if __name__ == "__main__":
    path = "/opt/trabalhos/etl-mdd/utils/ibge-codes/"
    input_text = path + "municipios.txt"
    output_csv = path + "municipios_code.csv"
    text_file_to_csv(input_text, output_csv)