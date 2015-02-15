# second_problem.py

languages = ["Python", "Ruby"]
languages = languages + ["C++", "Java", "C#"]
languages = ["Haskell"] + languages
languages = languages + ["Go"]

print(languages)

print(languages[0])
print(languages[1])
print(languages[4])

languages[5] = "F#"
print(languages)

last = len(languages) - 1
print(languages[last])

print("Haskell" in languages)
print("Ruby" in languages)
print("Go" in languages)
print("Rust" in languages)
