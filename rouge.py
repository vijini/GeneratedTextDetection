from rouge import FilesRouge

files_rouge = FilesRouge()
hyp_path = '/A88-1023-fake.txt'
ref_path = '/A88-1023.txt'
scores = files_rouge.get_scores(hyp_path, ref_path)
