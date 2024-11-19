def serialize_chat_history(chat_history):
    res = ""
    for chat_item in chat_history:
        role = chat_item["role"].strip()
        content = chat_item["content"].strip()
        res += f"[:ROLE={role}]{content}\n"
    return res.strip()
