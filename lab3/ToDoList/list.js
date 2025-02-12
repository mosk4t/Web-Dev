const parent = document.getElementById('list');
let a = '';
document.getElementById("add-button").onclick = function()
{
    let a = document.getElementById("myText");
    if (a.value)
    {
        const newObject = document.createElement('div');
        newObject.className = 'todo-element';
        
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox'; 
        checkbox.className = 'todo-checkbox';
        newObject.appendChild(checkbox);

        
        const text = document.createElement('span')
        text.className = 'todo-text';
        text.textContent = a.value;
        newObject.appendChild(text);
        
        const deleteButton = document.createElement('a');
        deleteButton.className = 'todo-delete';
        deleteButton.onclick = function()
        {
            newObject.remove();
        }

        checkbox.onclick = function() 
        {
            if (checkbox.checked){
                const delText = document.createElement('del');
                delText.textContent = text.textContent;
                delText.className = 'todo-text';
                text.remove();
                newObject.insertBefore(delText,deleteButton);
            }
            else
            {
                const delText = newObject.querySelector('del');
                if(delText)
                    delText.remove();
                newObject.insertBefore(text,deleteButton);
            }
        }
        const icon = document.createElement('i');
        icon.className = 'fa fa-trash';
        deleteButton.appendChild(icon);
        newObject.appendChild(deleteButton);
        
        
        parent.appendChild(newObject);
        a.value = '';
    }
}