import json
import csv


if __name__ == "__main__":
    input_json_path = "C:\\Users\\Beatr\\Documents\\etl-mdd\\csv-files\\"
    file_name = "bolsa-familia2021.json"
    input_path = input_json_path + file_name
    output_csv_file = "bolsa-familia2021.csv"
    data = {}

    with open(input_path, 'r') as file:
        data = json.load(file)

    docs = data["response"]["docs"]

    with open(output_csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(["ibge", "anomes", "qtd_familias_beneficiarias_bolsa_familia", "valor_repassado_bolsa_familia"])
        
        for doc in docs:
            writer.writerow([
                doc.get("ibge", ""),
                doc.get("anomes", ""),
                doc.get("qtd_familias_beneficiarias_bolsa_familia", ""),
                doc.get("valor_repassado_bolsa_familia", "")
            ])

    print("Finished transforming json content in a csv file")