import hashlib

def double_sha256(data):
    return hashlib.sha256(hashlib.sha256(data.encode()).digest()).hexdigest()


tx_hashes = [
    "a1b2c3d4",
    "b5c6d7e8",
    "c9d0e1f2",
    "d3e4f5a6"
]

print("Transaction Hashes:")
for tx in tx_hashes:
    print(tx)
print("\n")


hash_ab = double_sha256(tx_hashes[0] + tx_hashes[1])
hash_cd = double_sha256(tx_hashes[2] + tx_hashes[3])

print(f"Hash(AB): {hash_ab}")
print(f"Hash(CD): {hash_cd}")

# Compute Merkle root
merkle_root = double_sha256(hash_ab + hash_cd)
print(f"\nMerkle Root: {merkle_root}")

# Save output
with open("merkle_tree_output.txt", "w") as f:
    f.write(f"Merkle Root: {merkle_root}\n")

