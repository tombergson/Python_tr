fav_langs = {
    'johny': 'python',
    'elen': 'java',
    'tom': 'c++',
    'vanda': 'python',
}


print("W ankiecie zostału wymienione następujące jezyki programowania:")
for lang in set(fav_langs.values()): #jezeli wpiszemy set(fav_langs.values()) uzyskamy tylko unikatowe elementy.
    print(lang.title())