import { Button } from "@/components/ui/button";
import Link from "next/link"; // Import correto para navegação no Next.js

export const Hero = () => {
  return (
    <div className="flex flex-col items-center justify-center min-h-[80vh] text-center px-4">
      <h1 className="text-4xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-primary to-warning bg-clip-text text-transparent">
        Pare de desperdiçar comida
      </h1>
      <p className="text-xl md:text-2xl text-gray-600 mb-8 max-w-2xl">
        Economize mais de R$100,00 por mês com nosso assistente inteligente que
        monitora validades e sugere receitas personalizadas.
      </p>
      <div className="space-x-4">
        <Button asChild size="lg" className="bg-primary hover:bg-primary/90">
          <Link href="/produtos">Começar Agora</Link>
        </Button>
        <Button
          asChild
          variant="outline"
          size="lg"
          className="border-primary text-primary hover:bg-primary/10"
        >
          <Link href="/como-funciona">Saiba Mais</Link>
        </Button>
      </div>
    </div>
  );
};