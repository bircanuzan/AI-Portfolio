const form = document.querySelector('#chat-form');
const input = document.querySelector('#question');
const token = document.querySelector('#token');
const messages = document.querySelector('#messages');
const status = document.querySelector('#status');
const submit = document.querySelector('#submit');
function append(text, css) {
  const item = document.createElement('div'); item.className = 'message ' + css;
  item.textContent = text; messages.appendChild(item); messages.scrollTop = messages.scrollHeight;
}
form.addEventListener('submit', async (event) => {
  event.preventDefault();
  if (!token.value || !input.value.trim()) { status.textContent = 'Access token and question required.'; return; }
  const question = input.value.trim(); append(question, 'user'); input.value = '';
  submit.disabled = true; status.textContent = 'Checking policy and model...';
  try {
    const response = await fetch('/api/chat', {
      method: 'POST', headers: {'Authorization': 'Bearer ' + token.value, 'Content-Type': 'application/json'},
      body: JSON.stringify({question})
    });
    const data = await response.json();
    if (!response.ok) { append('Request not completed: ' + (data.detail || 'Service unavailable'), 'error'); return; }
    const citation = data.policy_ids.length ? 'Sources: ' + data.policy_ids.join(', ') + '. ' : '';
    append(data.answer + '\n\n' + citation + data.note, 'assistant');
  } catch (_) { append('Cannot reach the protected API. Check deployment status.', 'error'); }
  finally { submit.disabled = false; status.textContent = ''; }
});
