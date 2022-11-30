from knora import excel2xml


def main():
    # create an XML with 1000 plain resources that have x text fields and x links to another resource
    for x in range(5):
        root = excel2xml.make_root(shortcode="4124", default_ontology="xmlperformance")
        root = excel2xml.append_permissions(root)
        for i in range(1000):
            resource = excel2xml.make_resource(
                label=f"resource_{i}",
                restype=":PlainResource",
                id=f"resource_{i}"
            )
            if x:
                resource.append(excel2xml.make_text_prop(":hasText", [f"text field {n} of resource_{i}" for n in range(x)]))
            targets = [f"resource_{(i + 1 + n) % 1000}" for n in range(x)]
            if targets:
                resource.append(excel2xml.make_resptr_prop(":hasLink", targets))
            root.append(resource)
        excel2xml.write_xml(root, f"../xml_files/no_files_{x}_links_{x}_textfields.xml")


if __name__ == "__main__":
    main()
