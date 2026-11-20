from fastembed import TextEmbedding
for m in TextEmbedding.list_supported_models():
    print(m["model"], m["dim"], m.get("size_in_GB"))