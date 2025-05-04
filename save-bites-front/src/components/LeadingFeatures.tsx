import { Card, CardContent } from "@/components/ui/card";
import { Bell, List, ShoppingCart } from "lucide-react";

export const LandingFeatures = () => {
  const features = [
    {
      icon: Bell,
      title: "Alertas Inteligentes",
      description:
        "Receba notificações antes que seus alimentos percam a validade",
    },
    {
      icon: List,
      title: "Receitas Personalizadas",
      description:
        "Sugestões de receitas baseadas nos ingredientes que você tem em casa",
    },
    {
      icon: ShoppingCart,
      title: "Lista de Compras",
      description:
        "Gerencie suas compras de forma inteligente e evite desperdício",
    },
  ];

  return (
    <div className="py-16 bg-gray-50 flex items-center justify-center">
      <div className="container">
        <h2 className="text-3xl font-bold text-center mb-12">
          Como podemos te ajudar
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {features.map((feature) => (
            <Card key={feature.title} className="border-none shadow-lg">
              <CardContent className="pt-6">
                <div className="flex flex-col items-center text-center">
                  <div className="p-3 bg-primary/10 rounded-full mb-4">
                    <feature.icon className="w-6 h-6 text-primary" />
                  </div>
                  <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>
                  <p className="text-gray-600">{feature.description}</p>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </div>
  );
};