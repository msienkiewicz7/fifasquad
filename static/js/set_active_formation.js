// sets active formation if specified in url query

const urlParams = new URLSearchParams(window.location.search);
const p = urlParams.get('p');
if (p) {
  const option = document.querySelector(`option[value=\"${p}\"]`)
  option.selected = "selected"
}
