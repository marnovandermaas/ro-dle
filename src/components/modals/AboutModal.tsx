import { BaseModal } from './BaseModal'

type Props = {
  isOpen: boolean
  handleClose: () => void
}

export const AboutModal = ({ isOpen, handleClose }: Props) => {
  return (
    <BaseModal title="About" isOpen={isOpen} handleClose={handleClose}>
      <p className="text-sm text-gray-500 dark:text-gray-300">
        Aceasta este o versiune open source a jocului de ghicit cuvinte pe care
        il stim si il iubim cu totii -{' '}
        <a
          href="https://github.com/marnovandermaas/ro-dle"
          className="underline font-bold"
        >
          codul poate fi gasit aici
        </a>{' '}
      </p>
    </BaseModal>
  )
}
