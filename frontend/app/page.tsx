import Image from "next/image";

export default async function Home() {
  const response = await fetch('http://localhost:8000/', { 
    cache: 'no-store' 
  });

  return (
    <>Welcome to Recipe App</>
  );
}
