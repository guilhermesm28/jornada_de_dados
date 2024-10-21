 -- Visualização de cadastros
select
  *
from
  produto;

-- Inclusão de uma venda
insert into
  registrovendas (cod_prod, qtde_vendida)
values
  (1, 5);

insert into
  registrovendas (cod_prod, qtde_vendida)
values
  (3, 16);
