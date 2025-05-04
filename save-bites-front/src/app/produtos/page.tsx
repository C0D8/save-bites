"use client"
import { useEffect, useState } from 'react';
import { Button } from "@/components/ui/button";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { Plus, CircleCheck, Circle, CircleAlert, MoreHorizontal } from "lucide-react";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import Link from "next/link";

const mockProdutos = [
  {
    id: 1,
    nome: "Queijo Mussarela",
    dataCompra: "2024-04-20",
    dataValidade: "2024-05-05",
    quantidade: 5,
  },
  {
    id: 2,
    nome: "Presunto",
    dataCompra: "2024-04-21",
    dataValidade: "2024-04-28",
    quantidade: 2,
  },
];

const ListarProdutos = () => {
  const [isClient, setIsClient] = useState(false);

  useEffect(() => {
    setIsClient(true); // Define isClient para true após o cliente carregar
  }, []);

  const formatarData = (data: string) => {
    return new Date(data).toLocaleDateString("pt-BR");
  };

  const getStatusIcon = (dataValidade: string, quantidade: number) => {
    const hoje = new Date();
    const validade = new Date(dataValidade);
    const diasAteVencer = Math.ceil((validade.getTime() - hoje.getTime()) / (1000 * 60 * 60 * 24));

    if (quantidade <= 2) {
      return <CircleAlert className="w-4 h-4 text-destructive" />;
    } else if (diasAteVencer <= 0) {
      return <CircleAlert className="w-4 h-4 text-destructive" />;
    } else if (diasAteVencer <= 7) {
      return <Circle className="w-4 h-4 text-warning" />;
    } else {
      return <CircleCheck className="w-4 h-4 text-primary" />;
    }
  };

  const handleRemover = (id: number) => {
    console.log('Removendo produto:', id);
  };

  const handleEditar = (id: number) => {
    console.log('Editando produto:', id);
  };

  return (
    <div className="container max-w-4xl mx-auto py-10">
      <div className="flex justify-between items-center mb-8">
        <div>
          <h1 className="text-3xl font-bold">Meus Produtos</h1>
          <p className="text-gray-600 mt-2">
            Gerencie seus produtos e suas datas de validade
          </p>
        </div>
        <Button asChild>
          <Link href="/cadastrar-produto">
            {isClient && <Plus className="w-4 h-4 mr-2" />}
            Novo Produto
          </Link>
        </Button>
      </div>

      <div className="rounded-lg border">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Status</TableHead>
              <TableHead>Nome</TableHead>
              <TableHead>Quantidade</TableHead>
              <TableHead>Data da Compra</TableHead>
              <TableHead>Data de Validade</TableHead>
              <TableHead className="w-[50px]"></TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {mockProdutos.map((produto) => (
              <TableRow key={produto.id}>
                <TableCell className="w-[50px]">
                  {getStatusIcon(produto.dataValidade, produto.quantidade)}
                </TableCell>
                <TableCell>{produto.nome}</TableCell>
                <TableCell>{produto.quantidade}</TableCell>
                <TableCell>{formatarData(produto.dataCompra)}</TableCell>
                <TableCell>{formatarData(produto.dataValidade)}</TableCell>
                <TableCell>
                  <DropdownMenu>
                    <DropdownMenuTrigger asChild>
                      <Button variant="ghost" className="h-8 w-8 p-0">
                        <MoreHorizontal className="h-4 w-4" />
                      </Button>
                    </DropdownMenuTrigger>
                    <DropdownMenuContent align="end">
                      <DropdownMenuItem onClick={() => handleEditar(produto.id)}>
                        Editar
                      </DropdownMenuItem>
                      <DropdownMenuItem 
                        onClick={() => handleRemover(produto.id)}
                        className="text-destructive"
                      >
                        Remover
                      </DropdownMenuItem>
                    </DropdownMenuContent>
                  </DropdownMenu>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    </div>
  );
};

export default ListarProdutos;