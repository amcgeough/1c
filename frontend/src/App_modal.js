import React from 'react';

//import Popover from 'react-bootstrap/lib/Popover';
import Button from 'react-bootstrap/lib/Button';
import Modal from 'react-bootstrap/lib/Modal';
//import Tooltip from 'react-bootstrap/lib/Tooltip';
//import OverlayTrigger from 'react-bootstrap/lib/OverlayTrigger';

let rand = ()=> (Math.floor(Math.random() * 35) - 10);

const modalStyle = {
  position: 'fixed',
  zIndex: 1040,
  top: 0, bottom: 0, left: 0, right: 0
};

const backdropStyle = {
  ...modalStyle,
  zIndex: 'auto',
  backgroundColor: '#000',
  opacity: 0.5
};

const dialogStyle = function() {
  // we use some psuedo random coords so nested modals
  // don't sit right on top of each other.
  let top = -20 + (rand());
  let left = 50 + (rand());

  return {
    position: 'absolute',
    width: 400,
    top: top + '%', left: left + '%',
    transform: `translate(-${top}%, -${left}%)`,
    border: '1px solid #e5e5e5',
    backgroundColor: 'white',
    boxShadow: '0 5px 15px rgba(0,0,0,.5)',
    padding: 20
  };
};


class ModalExample extends React.Component {

  constructor(props, context) {
    super(props, context);

    this.handleShow = this.handleShow.bind(this);
    this.handleClose = this.handleClose.bind(this);
    this.handleClose2 = this.handleClose2.bind(this);

    this.state = { showModal: false, showModal2: false, todos: [], choice: []};

  }


  handleShow() {
    this.setState({ showModal: true, showModal2: true });
  }

  handleClose() {
    this.setState({ showModal: false });
  }

  handleClose2() {
    this.setState({ showModal2: false });
  }

  async componentDidMount() {
 //using try and catch due to the api request
    try {
      const res = await fetch('http://127.0.0.1:8000/api/');
      const todos1 = await res.json();
      const todos = todos1.filter( element => element.id===3)

      this.setState({
        todos
      });
    } catch (e) {
      console.log(e);
    }

    try {
      const choice_api = await fetch('http://127.0.0.1:8000/api/choice');
      const choice1 = await choice_api.json();
      const choice = choice1.filter( element => element.question===3)
      console.log(choice)

      this.setState({
        choice
      });
    } catch (e) {
      console.log(e);
    }

  }




  render() {

    return (
      <div className='modal-example'>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossOrigin="anonymous" />

        <Button onClick={this.handleShow} >
          Open Modal
        </Button>
        <p>Click to get the full Modal experience!</p>

        <Modal
          aria-labelledby='modal-label'
          style={modalStyle}
          backdropStyle={backdropStyle}
          show={this.state.showModal}
          onHide={this.handleClose}
        >
            <div style={dialogStyle()} >
                <h4 id='modal-label'>Text in a modal</h4>
                <p>Duis mollis, est non commodo luctus, nisi erat porttitor ligula.</p>
                <ModalExample/>
                <Modal.Footer>
                  <Button onClick={this.handleClose}>Close</Button>
                </Modal.Footer>
            </div>
        </Modal>

        <Modal
          aria-labelledby='modal-label'
          style={modalStyle}
          backdropStyle={backdropStyle}
          show={this.state.showModal2}
          onHide={this.handleClose2}
        >
            <div style={dialogStyle()} >
                <h4 id='modal-label'>Text in a modal</h4>

                {this.state.todos.map(item => (
                <div key={item.id}>
                <h1>{item.question_text}</h1>
                </div>
                ))}

                {this.state.choice.map(item2 => (
                <div key={item2.id}>
                <li>{item2.choice_text}</li>
                </div>
                ))}


                <ModalExample/>
                <Modal.Footer>
                    <Button onClick={this.handleClose2}>Close</Button>
                </Modal.Footer>
            </div>
        </Modal>


        </div>
    );
  }

}

export default ModalExample;
//render(<ModalExample />);