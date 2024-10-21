-- Visualização de cadastros
select
  *
from
  funcionario;

-- Atualização de salário
update
  funcionario
set
  salario = 4300.00
where
  nome = 'Ana';

-- Validação do log de atualização
select
  *
from
  funcionario_auditoria;
