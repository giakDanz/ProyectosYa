import React from 'react'

const Navigation = () => {
    const handleClick = () => {
        console.log('abc');
    }
    return (
        <div className='navigation'>
            <ul className="center">
                <li>
                    <button className="btnYa infoya" onClick={handleClick}>InfoYa</button>
                </li>
                <li>
                    <button className="btnYa accionya" onClick="message()">AcciónYa</button>
                </li>
                <li>
                    <button className="btnYa preguntasya" onClick="message()">PreguntasYa</button>
                </li>
            </ul>
        </div>
    )
}

export default Navigation
