from flask import Flask, session, render_template_string
import filter  # 假设filter是一个自定义的过滤函数，需要导入
app = Flask(__name__)

@app.route('/nonono')
def source():
    f = open(__file__, 'r')
    rsp = f.read()
    f.close()
    return rsp[rsp.index('nonono'):]

@app.route('/admin')
def admin_handler():
    try:
        role = session.get('role')
        if not isinstance(role, dict):
            raise Exception
        if role.get('is_admin') == 1:
            flag = role.get('flag') or 'admin'
            flag = filter(flag)  
            message = "%s, God bless you! The flag is " % flag
            return render_template_string(message)
        else:
            return "Error: Permission denied!"
    except Exception:
        return 'No, you are a hacker!'

if __name__ == '__main__':
    app.run('0.0.0.0', port=80)
