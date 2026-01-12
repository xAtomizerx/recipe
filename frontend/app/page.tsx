import Image from "next/image";

export default async function Home() {
  const response = await fetch('https://recipe-9811nf6hf-atomizers-projects.vercel.app/', { 
    cache: 'no-store' 
  });

  return (
    <>Welcome to Recipe App</>
  );
}
