from flask import Flask, render_template, request, redirect
from models import db, Task
from ai_logic import calculate_priority
from flask import jsonify

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db.init_app(app)

# ✅ FIX: Create DB using app context
with app.app_context():
    db.create_all()

# Home
@app.route('/')
def index():
    tasks = Task.query.order_by(Task.priority.desc()).all()
    return render_template('index.html', tasks=tasks)

# Add task
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        urgency = int(request.form['urgency'])
        time_required = int(request.form['time'])

        priority = calculate_priority(urgency, time_required)

        task = Task(
            title=title,
            urgency=urgency,
            time_required=time_required,
            priority=priority
        )

        db.session.add(task)
        db.session.commit()

        return redirect('/')

    return render_template('add_task.html')

@app.route('/delete/<int:id>')
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_task(id):
    task = Task.query.get(id)

    if request.method == 'POST':
        task.title = request.form['title']
        task.urgency = int(request.form['urgency'])
        task.time_required = int(request.form['time'])

        from ai_logic import calculate_priority
        task.priority = calculate_priority(task.urgency, task.time_required)

        db.session.commit()
        return redirect('/')

    return render_template('update_task.html', task=task)
@app.route('/api/tasks')
def api_get_tasks():
    tasks = Task.query.all()

    data = []
    for t in tasks:
        data.append({
            "id": t.id,
            "title": t.title,
            "priority": t.priority,
            "urgency": t.urgency,
            "time_required": t.time_required
        })

    return jsonify(data)
@app.route('/api/tasks', methods=['POST'])
def api_add_task():
    data = request.json

    title = data['title']
    urgency = data['urgency']
    time_required = data['time_required']

    priority = calculate_priority(urgency, time_required)

    task = Task(
        title=title,
        urgency=urgency,
        time_required=time_required,
        priority=priority
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({"message": "Task created"})

if __name__ == '__main__':
    app.run(debug=True)