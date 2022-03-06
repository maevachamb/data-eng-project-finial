import React from 'react';
import axios from 'axios';

export default class Form extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            value: "",
            error: null,
            baseURL: 'http://localhost:5000/predict_toxicity?user_text=',
            toxicity_text: null,
            toxicity_results: null, 
        }

        axios.defaults.withCredentials = true

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
    }

    handleSubmit(event) {
        console.log('User Text: ' + this.state.value);
        event.preventDefault();
    }

    onClick = e => {
        axios.get(this.state.baseURL + this.state.value, { withCredentials: true }).then(res => {
                e.preventDefault()
                this.setState({ toxicity_text: res.data.text, toxicity_results: res.data.results })
                this.value = ""
        }

        ).catch(error => {
            this.setState({ error: error.message });
            console.error('An error occured!', error);
        })
    }

    render() {
        const result = this.state.toxicity_results;
        if (this.state.error) {
            return <h1>An error occured.</h1>
        }

        return (
            <div>
                <div className="App">
                    <form id="regForm" onSubmit={this.handleSubmit}>
                        <h1 id="register">The Toxicity Monitor</h1>
                        <div className="tab">
                            <h4>The Toxicity Monitor is a toxicity analysis application,which, given a piece of text, is able to determine if the text is toxic or not.
                            <br/><br/><b>Try it by writing something below.</b></h4>
                            <input id = "user_text" type="text" placeholder="Please write something here..." value={this.state.value} onChange={this.handleChange} name="user_text"/>
                            <br/>
                        </div>
                        <input type="submit" id="submit_" value="Send" onClick={this.onClick}/>
                    </form>
                </div>
                {result ?
                    <div id="result">
                        <h3> Toxicity results </h3> 
                            You  have submitted the following: <strong>{this.state.toxicity_text}</strong><br/>
                            Here is how the monitor interprets the sentence:
                            {Object.entries(result).map(([name, value]) => (
                            <p key={name}><strong>{name}</strong> is of {value}</p>
                            ))}   
                            {result['toxicity'] > 0.5 ?
                                <p>The text submitted is <strong>Toxic</strong></p>
                                :
                                <p>The text submitted is <strong>not Toxic</strong></p>
                            }
                    </div>
                    : null
                }
            </div>
        );

    }
}
