from create_train_folder import zip_extractor
from loader import image_reader

#zip_extractor('0325train_626p_data').expand_zip()
object_ls, annotation_ls = image_reader().create_dataset(path = '/0325updated_task1train_626p')
print(len(object_ls),len(annotation_ls))


