from Bio import SeqIO
def compute_gc(fasta_path):
    sequence_dict = {record.id: str(record.seq) for record in SeqIO.parse(fasta_path, "fasta")}
    max_gc_id = ""
    max_gc = 0
    gc_content_dict = {}

    for id, sequence in sequence_dict.items():
        gc_content = ((sequence.count("G") + sequence.count("C")) / len(sequence)) * 100
        gc_content_dict[id] = gc_content

        if gc_content > max_gc:
            max_gc = gc_content
            max_gc_id = id

    return max_gc_id, max_gc


compute_gc("C:/Users/janni/Desktop/Pythonkurs/test_fasta.txt")