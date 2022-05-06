import React from 'react'
const Navigation = () => {
    const handleClick = () => {
        console.log('abc');
    }
    return (
        <div className='navigation'>
            <button class="btn infoya" onClick={handleClick}>InfoYa</button>
            <button class="btn accionya" onClick="message()">AcciónYa</button>
            <button class="btn preguntasya" onClick="message()">PreguntasYa</button>
        </div>
    )
}

export default Navigation
