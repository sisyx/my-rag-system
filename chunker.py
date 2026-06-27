def chunk_text(data: str, chunk_size: int, overlap: int) -> list[str]:
    if chunk_size <= overlap:
        raise ValueError(f"overlap {overlap} must be less than the chunk_size")

    chunks_count = int(len(data) / chunk_size)
    chunks = []
    for chunk_num in range(1, chunks_count + 1):
        chunk_start = (chunk_num - 1) * chunk_size
        chunk_start = chunk_start if chunk_num == 1 else chunk_start - overlap
        chunk_end = chunk_num * chunk_size + overlap
        chunk_end = chunk_end - overlap if chunk_end > len(data) else chunk_end
        chunks.append(data[chunk_start:chunk_end])

    last_left_chunk = data[(chunks_count * chunk_size) :]
    if (len(last_left_chunk) != 0):
        chunks.append(last_left_chunk)

    return chunks
