const topicList = document.getElementById("topicList");
const form = document.getElementById("topicForm");

async function fetchTopics() {
  const res = await fetch("/topics");
  const topics = await res.json();
  topicList.innerHTML = "";
  topics.forEach(topic => {
    const li = document.createElement("li");
    li.textContent = `${topic.title} (${topic.subject}) - ${topic.notes || "No notes"}`;
    
    const delBtn = document.createElement("button");
    delBtn.textContent = "❌";
    delBtn.onclick = () => deleteTopic(topic._id);
    
    li.appendChild(delBtn);
    topicList.appendChild(li);
  });
}

form.onsubmit = async e => {
  e.preventDefault();
  const data = {
    title: form.title.value,
    subject: form.subject.value,
    notes: form.notes.value
  };
  await fetch("/topics", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data)
  });
  form.reset();
  fetchTopics();
};

async function deleteTopic(id) {
  await fetch(`/topics/${id}`, { method: "DELETE" });
  fetchTopics();
}

fetchTopics();
