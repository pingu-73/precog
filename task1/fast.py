import requests
import helper
import word2vec

Data_URL = "https://storage.googleapis.com/kagglesdsdata/datasets/635905/1130166/hp1.txt?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20240216%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240216T195714Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=83fe509bfac089a6b592146134b07fcf18866e7b2d1f9faeeed46a39142c0e2e7e189647d6dc83c7ac2d6c32d4687b84d73d37989a67aded877dfec9cb17da9043a7b9d90bc8e2c210be3fa6d7a2a5aedc4c7a1710bdff3310748e9b69098dc5250f6773a9e7902846ac7837b54baf25d20300a1b3a3ccbdfaf93fb7438bae9ba73ad9400871847bd6776b5d80e272e5405fba7fcbc1d2a349452b000b6d9aa598800006bd04e6312a5f3f1f76bcb7fe8807cfb83850c0148ab85136d13b9fcebc0c641b660820c3926675f4f2332c6bdce2ff4cf846651ad8bef3f3dd8516c6dd511d3aa51906302a0559e4c1bd5c51409724c83ce854f01f86923536b9b503"
r = requests.get(Data_URL)
text = r.text

tokens = helper.tokenize(text)
word_to_id, id_to_word = helper.mapping(tokens)
X, y = word2vec.generate_training_data(tokens, word_to_id, 2)

print(X.shape)
print(y.shape)