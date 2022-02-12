import { Cell } from '../grid/Cell'
import { BaseModal } from './BaseModal'

type Props = {
  isOpen: boolean
  handleClose: () => void
}

export const InfoModal = ({ isOpen, handleClose }: Props) => {
  return (
    <BaseModal
      title="Regulile jocului"
      isOpen={isOpen}
      handleClose={handleClose}
    >
      <p className="text-sm text-gray-500 dark:text-gray-300">
        Ghiceste cuvantul din 6 incercari. Dupa fiecare incercare, culoarea
        patratelor se va schimba depinzand de cat de aproape ai fost de a ghici
        cuvantul.
      </p>

      <div className="flex justify-center mb-1 mt-4">
        <Cell value="S" status="correct" />
        <Cell value="C" />
        <Cell value="A" />
        <Cell value="U" />
        <Cell value="N" />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-300">
        Litera S se afla in cuvant si este in pozitia corecta.
      </p>

      <div className="flex justify-center mb-1 mt-4">
        <Cell value="P" />
        <Cell value="I" />
        <Cell value="L" status="present" />
        <Cell value="O" />
        <Cell value="T" />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-300">
        Litera L se afla in cuvant dar este in pozitia gresita.
      </p>

      <div className="flex justify-center mb-1 mt-4">
        <Cell value="M" />
        <Cell value="I" />
        <Cell value="N" />
        <Cell value="G" status="absent" />
        <Cell value="E" />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-300">
        Litera G nu se afla in cuvant.
      </p>
    </BaseModal>
  )
}
