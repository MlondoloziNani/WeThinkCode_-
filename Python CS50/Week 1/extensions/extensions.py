extension = input("File nume: ").lower().replace(" ","").split(".")[-1::]
extension = "".join(extension)

match extension:
    case "gif" | "png":
        print("image/" + extension)
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "pdf" | "zip":
        print("application/" + extension)
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")
