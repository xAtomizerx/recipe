import Image from "next/image";

export default async function Home() {
  const response = await fetch('https://recipe-two-jet.vercel.app/', { 
    cache: 'no-store' 
  });

  return (
    <>Welcome to Recipe App</>
  );
}
