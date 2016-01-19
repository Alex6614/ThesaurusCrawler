with open('handpicked_words.txt') as fp:
	result = ""
	for line in fp:
		newline = line.rstrip('\r\n')
		result += "scrapy crawl thesaurusspider -a start_url=%s -o %s.json & " %(newline, newline)
	result = result[:-2]
	print result