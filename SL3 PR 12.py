# Simple MapReduce simulation for word count

def mapper(text):
    words = text.split()
    return [(word, 1) for word in words]

def reducer(mapped_data):
    result = {}

    for word, count in mapped_data:
        result[word] = result.get(word, 0) + count

    return result

# Sample log data
log_data = "error warning error info error warning"

mapped = mapper(log_data)

reduced = reducer(mapped)

print("Word Count:", reduced)