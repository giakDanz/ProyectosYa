import Modal from 'react-bootstrap/Modal'
import React, {useState} from 'react'
import Button from 'react-bootstrap/Table'
const ModalElement = () => {
    const [show, setShow] = useState(false);

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    return (
        <>
            <Button className="light" onClick={handleShow}>
                Prueba 1
            </Button>

            <Modal show={show} onHide={handleClose}>
                <Modal.Header closeButton>
                    <Modal.Title>Prueba 1</Modal.Title>
                </Modal.Header>
                <Modal.Body>Info de proyecto 'Prueba 1'</Modal.Body>
                <Modal.Footer>
                    <Button className="btn-outline-primary btn-sm" onClick={handleClose}>
                        Cerrar
                    </Button>
                </Modal.Footer>
            </Modal>
        </>
    );
}

export default ModalElement
