import Image from 'next/image'
import logo from '../../app/resources/RV_Logo.png'
import '../globals.css'
import AuthRedirect from "../components/AuthRedirect"

export default function Header() {
    return(
        <div id='Header' className='text-4xl text-white p-4 flex justify-between items-center'>
            <div id='Title' className='font-bold background p-2 rounded'>
            <Image src={logo} alt='Logo' width={400} height={150} className='inline-block mr-2'/>
            </div>
            <div id='AuthLinks' className='flex space-x-4 items-center'>
            <AuthRedirect type="login"/>
            </div>
        </div>
    )
}