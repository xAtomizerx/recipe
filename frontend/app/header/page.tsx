import React from "react"
import '../globals.css'
import AuthRedirect from "../components/AuthRedirect"

export default function Header() {
    return(
        <div id='Header' className='text-4xl text-white p-4 flex justify-between items-center'>
            <div id='Title' className='font-bold background p-2 rounded'>
            Hello World
            </div>
            <div id='AuthLinks' className='flex space-x-4 items-center'>
            <AuthRedirect type="login" />
            </div>
        </div>
    )
}