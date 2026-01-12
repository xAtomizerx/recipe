import Image from "next/image";

export default async function Home() {
  const response = await fetch('https://gokvsygolwnixgyodtsi.supabase.co/', { 
    cache: 'no-store' 
  });

  return (
    <>Welcome to Recipe App</>
  );
}
