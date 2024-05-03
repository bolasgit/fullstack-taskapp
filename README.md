## Folder/ Directory convention for FastAPI For Frontend

1. Create your Static folder inside the project directory
2. Within the static folder, create another folder with a naming convention related to what you want to build
3. Within the folder which in this case we will call Todo, create your js and css folder

4. Within the css folder we will create a new css file called base.css which will hold the css code

##### Be sure to mount your static folder in the main.py file with the following code :

```
app.mount("/static", StaticFiles(directory="static"), name="static")
```

- Also include the path to base.css in the link of the html header thus:

```
<link
      rel="stylesheet"
      type="text/css"
      href="{{ url_for('static', path='todo/css/base.css') }}"
/>
```

- Same for the bootstrap.css in the link of the html header thus:

```
<link
      rel="stylesheet"
      type="text/css"
      href="{{ url_for('static', path='todo/css/bootstrap.css') }}"
/>
```

- These will allow us access our styling in the html file
- We will include a bootstrap specific meta tag to make the web app responsive:

```
<meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
/>
```

- For js scripts, they must be arrange in this order:

```
<script src="{{ url_for('static', path='todo/js/jquery-slim.js') }}"></script>
<script src="{{ url_for('static', path='todo/js/popper.js') }}"></script>
<script src="{{ url_for('static', path='todo/js/bootstrap.js') }}"></script>
```

#### HTML TAGS

- th - Table header
- tr - Table row
- td - Table data
- tbody - table body

- div class="container>> card>> card-header>> card-body>> form-group>> label>> field type

### Using jinja templating for abstraction

1. Create a file to hold reusable code ie header, navbar and footer
2. Within this file, in between the header and the footer, where the the main content for the page should lay, use the following code:

```
{% block content %} {% endblock %}
```

3. Next, in each of the pages which will require the reusable code ie the header and footer, you use the following code at the top of the page:

```
{% include 'name-of-html-page-holding-the-template-code.html%}
```

4. Using operators `{% for loop%}` and `{% end for %}` while `{{ variable}}` holds the variable form the function.
5. Buttons that hold redirection often hve this structure:

```
<button onclick="window.location.href='edit-todo/{{todo.owner_id}}'" type="button" class="btn btn-info">
```

6. We must also edit the from method to indicate it is a post or get request thus `<form method = "POST">`
7.
