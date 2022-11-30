from knora import excel2xml


def main():
    # create an XML with 1000 of the same JPEG with 1 MB size
    root = excel2xml.make_root(shortcode="4124", default_ontology="xmlperformance")
    root = excel2xml.append_permissions(root)
    for i in range(1000):
        identifier = f"_1MB_image_resource_{i}"
        resource = excel2xml.make_resource(
            label=identifier,
            restype=":ImageThing",
            id=identifier
        )
        resource.append(excel2xml.make_bitstream_prop("../bitstreams/1.jpeg"))
        resource.append(excel2xml.make_text_prop(":hasText", f"text field of {identifier}"))
        root.append(resource)
    excel2xml.write_xml(root, "../xml_files/one_file.xml")


if __name__ == "__main__":
    main()
