import json

# Define o caminho do arquivo JSON de entrada e do arquivo C# de saída
json_file_path = ".\input.json"
cs_file_path = ".\output.cs"

# Abre o arquivo JSON e carrega os dados em um objeto Python
with open(json_file_path) as json_file:
    data = json.load(json_file)

# Abre o arquivo C# para escrita e define a classe e o namespace
with open(cs_file_path, "w") as cs_file:
    cs_file.write("namespace MyApp\n{\n")
    cs_file.write("    /// <summary>\n    /// DEFINA O TO \n    /// </summary>\n")
    cs_file.write("    public class MyClass\n    {\n")

    # Itera sobre as chaves do objeto Python e escreve as propriedades C#
    for key in data:
        # Define o xmlAttribute e o summary
        xml_attr = "[XmlAttribute(\"{0}\")]".format(key)
        summary = "/// <summary>\n        /// {0}\n        /// </summary>".format(key)

        # Escreve a propriedade C# com o xmlAttribute e o summary
        cs_file.write("        {0}\n        {1}\n".format(summary, xml_attr))
        cs_file.write("        public {0} {1} {{ get; set; }} \n\n".format(type(data[key]).__name__, key))

    # Fecha a classe e o namespace
    cs_file.write("    }\n")
    cs_file.write("}\n")