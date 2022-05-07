import React from 'react'
import Table from 'react-bootstrap/Table'
const TableElements = ({children}) => {
    return (
        <div className='main center'>
            <Table className="table-hover table-responsive-lg">
                <thead>
                    <tr>
                        <th>Nombre del Proyecto</th>
                        <th>Expediente Tecnico</th>
                        <th>% Avance</th>
                        <th>Fecha de Viabilidad</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>
                            {children}
                        </td>
                        <td>Si</td>
                        <td>50%</td>
                        <td>01/01/1901</td>
                    </tr>
                </tbody>
            </Table>
        </div>
    )
}

export default TableElements
