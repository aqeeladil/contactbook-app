# myproject/myapp/templates/registration/login.html
<h2>Login</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Login</button>
</form>
<a href="{% url 'register' %}">Don't have an account? Register</a>


# myproject/myapp/templates/registration/register.html
<h2>Register</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Register</button>
</form>
<a href="{% url 'login' %}">Already have an account? Login</a>


# myproject/myapp/templates/contacts/contact_list.html
<h2>Your Contacts</h2>

<div style="display: flex;">
    <form method="get" style="display: inline;">
        <input type="text" name="q" placeholder="Search by name or email" value="{{ request.GET.q }}">
        <button type="submit">Search</button>
    </form>

    {% if request.GET.q %}
        <a href="{% url 'contact_list' %}" style="margin-left: 10px;">Clear Search</a>
    {% endif %}
</div>

<div style="margin-top: 7px;">
    <a href="{% url 'add_contact' %}">Add Contact</a>
    <form method="post" action="{% url 'logout' %}" style="display:inline; margin-left: 10px;">
        {% csrf_token %}
        <button type="submit">Logout</button>
    </form>
</div>


<div>
    <ul>
        {% for contact in contacts %}
            <li>
                <a href="{% url 'view_contact' contact.pk %}">{{ contact.name }}</a> - {{ contact.email }}
                [<a href="{% url 'update_contact' contact.pk %}">Edit</a>]
                [<a href="{% url 'delete_contact' contact.pk %}">Delete</a>]
            </li>
        {% empty %}
            <li>No contacts found.</li>
        {% endfor %}
    </ul>
</div>


# myproject/myapp/templates/contacts/contact_form.html
<h2>{{ form.instance.pk|yesno:"Update Contact,Add Contact" }}</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Save</button>
</form>
<a href="{% url 'contact_list' %}">Back</a>


# myproject/myapp/templates/contacts/contact_detail.html
<h2>Contact Details</h2>

<p><strong>Name:</strong> {{ contact.name }}</p>
<p><strong>Email:</strong> {{ contact.email }}</p>
<p><strong>Phone:</strong> {{ contact.phone }}</p>
<p><strong>Address:</strong> {{ contact.address }}</p>

<a href="{% url 'update_contact' contact.pk %}">Edit</a> |
<a href="{% url 'contact_list' %}">Back to List</a>


# myproject/myapp/templates/contacts/contact_confirm_delete.html
<h2>Delete Contact</h2>
<p>Are you sure you want to delete "{{ contact.name }}"?</p>
<form method="post">
  {% csrf_token %}
  <button type="submit">Yes, delete</button>
</form>
<a href="{% url 'contact_list' %}">Cancel</a>


