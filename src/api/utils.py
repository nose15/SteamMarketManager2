def read_json_file(json_file_path: str) -> str:
    json_str = ""

    with open(json_file_path, "r") as file:
        lines = file.readlines()

        for line in lines:
            line.strip(" ")
            line.strip("\n")

            json_str += line

        file.close()

    return json_str
