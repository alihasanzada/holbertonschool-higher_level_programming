document.querySelector('DIV#add_item').addEventListener('click', function () {
  const item = document.createElement('li');
  item.textContent = 'Item';
  document.querySelector('UL.my_list').appendChild(item);
});
