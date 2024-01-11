class Tagger:
    def __init__(self, file_name, size, tags):
        self.file_name = file_name
        self.tags = tags
        self.size = size


def get_total_size(files):
    return sum(file.size for file in files)


def get_top_tags(files, n):
    tag_count = {}
    for file in files:
        for tag in file.tags:
            tag_count[tag] = tag_count.get(tag, 0) + 1
    sorted_tags = sorted(tag_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_tags[:n]


if __name__ == '__main__':
    files = [
        Tagger("document1.txt", 100, ["report", "data"]),
        Tagger("image.jpg", 500, ["image", "design"]),
        Tagger("spreadsheet.xlsx", 200, ["report", "data"]),
        Tagger("code.py", 50, ["code", "programming"]),
        Tagger("presentation.pptx", 300, ["report", "presentation"]),
    ]

    # Calculate and print statistics
    print(f"Total size of files: {get_total_size(files)} bytes")

    n = 2  # Change this value to get the top n tags
    top_tags = get_top_tags(files, n)
    print(f"Top {n} tags:")
    for tag, count in top_tags:
        print(f"{tag}: {count} files")
