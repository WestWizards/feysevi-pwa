import React from "react"
import {Layout, Form, Input, Checkbox, Button} from "antd"
import {Link} from "react-router-dom"
import logo from "../../logo.svg"

export default class Login extends React.Component {
	_doLogin = () => {
		console.log("logged")
	}
	
	render() {
		return <Layout>
			<Layout.Content>
				<img src={logo} alt="Logo"/>
				<h1 style={{textAlign: "center"}}> Hey, t'es de retour ?
					<br/>
					<small>Connecte-toi pour continuer</small>
				</h1>
				<Form onSubmit={this._doLogin}>
					<Form.Item>
						<Input placeholder="Username"/>
					</Form.Item>
					<Form.Item>
						<Input type="password" placeholder="Password"/>
					</Form.Item>
					<Form.Item>
						<Link className="login-form-forgot" to="/alzheimer">Forgot password</Link>
					</Form.Item>
					<Form.Item>
						<Button type="primary" htmlType="submit" className="login-form-button">
							Log in
						</Button>
						<p style={{textAlign: 'center', lineHeight: "14pt"}}>Première visite ? <Link to="/">Découvre le concept</Link></p>
					</Form.Item>
				</Form>
			</Layout.Content>
		</Layout>
	}
}