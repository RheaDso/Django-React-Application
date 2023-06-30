import React, { Component } from 'react';
import axios from 'axios';
// import { Alert } from 'react-alert';
// import { confirmAlert } from 'react-confirm-alert';

class App extends Component {


  state = {
    title: '',
    content: '',
    image: null
  };

  handleChange = (e) => {
    this.setState({
      [e.target.id]: e.target.value
    })
  };

  handleImageChange = (e) => {
    this.setState({
      image: e.target.files[0]
    })
  };

  handleSubmit = (e) => {

      console.log("Handle1")
      fetch("http://127.0.0.1:8000/api-predict/predict-test/")
      .then(response => {
        console.log('Success:', response);
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        console.log("Handle2")
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });  

    // e.preventDefault();
    // console.log(this.state);
    // let form_data = new FormData();
    // form_data.append('image', this.state.image, this.state.image.name);
    // form_data.append('title', this.state.title);
    // form_data.append('content', this.state.content);
    // let url = 'http://localhost:8000/api-post/posts/';
    // axios.post(url, form_data, {
    //   headers: {
    //     'content-type': 'multipart/form-data'
    //   }
    // })
    //     .then(res => {
    //       console.log(res.data);
    //     })
    //     .catch(err => console.log(err))
  };

  render() {
    return (
      <div className="App">
        <form onSubmit={this.handleSubmit}>
          <p>
            <input type="text" placeholder="Title 1" id='title' value={this.state.title} onChange={this.handleChange} required/>
          </p>
          <p>
            <input type="text" placeholder="Content 2" id='content' value={this.state.content} onChange={this.handleChange} required/>

          </p>
          <p>
            <input type="file" placeholder="Save"
                   id="image"
                   accept="image/png, image/jpeg"  onChange={this.handleImageChange} required/>
          </p>
          <input type="submit"/>
        
        </form> 
      </div>
      

    );
  }
}

export default App;

