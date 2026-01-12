import Image from 'next/image'
import '../globals.css'
import AuthRedirect from "../components/AuthRedirect"

export default function Header() {
    return(
        <div id='Header' className='text-4xl text-white p-4 flex justify-between items-center'>
            <div id='Title' className='font-bold background p-2 rounded'>
            <Image src='resources/RV_Logo.png' alt='Logo' width={150} height={100} className='inline-block mr-2'/>
            </div>
            <div id='AuthLinks' className='flex space-x-4 items-center'>
            <AuthRedirect type="signup"/>
            </div>
        </div>
    )
}